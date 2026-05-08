# IsBackgroundProcessingCompleted Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsBackgroundProcessingCompleted`

Gets whether SOLIDWORKS has finished background processing a drawing document that requires a lot of CPU time to open.
Gets whether SOLIDWORKS has finished background processing a drawing document that requires a lot of CPU time to open.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsBackgroundProcessingCompleted( _
   ByVal FilePath As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim FilePath As System.String
Dim value As System.Boolean
 
value = instance.IsBackgroundProcessingCompleted(FilePath)
```

```

System.bool IsBackgroundProcessingCompleted( 
   System.string FilePath
)
```

```

System.bool IsBackgroundProcessingCompleted( 
   System.String^ FilePath
) 
```

#### Parameters

*FilePath*
:   Fully qualified path and filename of the drawing document that was opened in a background process

#### Return Value

True if background processing is finished, false if not

Remarks

SOLIDWORKS recommends that you only use this method with [ISldWorks::EnableBackgroundProcessing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnableBackgroundProcessing.md) and [IDrawingDoc::BackgroundProcessingOption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~BackgroundProcessingOption.md) when you can quickly open a drawing document via the user interface, but that same drawing takes significantly more time to open programmatically.

To more efficiently and programmatically open a drawing document that requires a lot of CPU time and no user input:

1. Set ISldWorks::EnableBackgroundProcessing to true.
2. Use [ISldWorks Event BackgroundProcessingStartNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_BackgroundProcessingStartNotifyEventHandler.md) to handle the background processing start event.
3. Open the drawing document by calling either [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md) or [ISldWorks::OpenDoc7](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.md).
4. Set IDrawingDoc::BackgroundProcessingOption to [swBackgroundProcessOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBackgroundProcessOption_e.html).swBackgroundProcessing\_DeferToApplication.
5. Call ISldWorks::IsBackgroundProcessingCompleted repeatedly, which polls the status of the open operation, to know when background processing ends.
6. Use [ISldWorks Event BackgroundProcessingEndNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_BackgroundProcessingEndNotifyEventHandler.md) to handle the background processing end event.
7. When the open operation is finished, set ISldWorks::EnableBackgroundProcessing to false.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
