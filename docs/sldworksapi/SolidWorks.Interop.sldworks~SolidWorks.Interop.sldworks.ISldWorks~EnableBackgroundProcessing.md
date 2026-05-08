# EnableBackgroundProcessing Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnableBackgroundProcessing`

Gets or sets whether to enable background processing.
Gets or sets whether to enable background processing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EnableBackgroundProcessing As System.Boolean
```

```

Dim instance As ISldWorks
Dim value As System.Boolean
 
instance.EnableBackgroundProcessing = value
 
value = instance.EnableBackgroundProcessing
```

```

System.bool EnableBackgroundProcessing {get; set;}
```

```

property System.bool EnableBackgroundProcessing {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enable background processing, false to not

Remarks

SOLIDWORKS recommends that you only use this property with [ISldWorks::IsBackgroundProcessingCompleted](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsBackgroundProcessingCompleted.md) and [IDrawingDoc::BackgroundProcessingOption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~BackgroundProcessingOption.md) when you can quickly open a drawing document via the user interface, but that same drawing takes significantly more time to open programmatically.

To more efficiently and programmatically open a drawing document that requires a lot of CPU time and no user input:

1. Set ISldWorks::EnableBackgroundProcessing to true.
2. Use [ISldWorks Event BackgroundProcessingStartNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_BackgroundProcessingStartNotifyEventHandler.md) to handle the background processing start event.
3. Open the drawing document by calling either [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md) or [ISldWorks::OpenDoc7](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.md).
4. Set IDrawingDoc::BackgroundProcessingOption to [swBackgroundProcessOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBackgroundProcessOption_e.html).swBackgroundProcessing\_DeferToApplication.
5. Call ISldWorks::IsBackgroundProcessingCompleted repeatedly, which polls the status of the open operation, to know when background processing ends.
6. Use [ISldWorks Event BackgroundProcessingEndNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_BackgroundProcessingEndNotifyEventHandler.md) to handle the background processing end event.
7. When the open operation is finished, set ISldWorks::EnableBackgroundProcessing to false.

Example

[Fire Notifications for Background Processing Events (VBA)](Fire_Notification_for_Background_Processing_Events_Example_VB.htm)  
[Fire Notifications for Background Processing Events (VB.NET)](Fire_Notification_for_Background_Processing_Events_Example_VBNET.htm)  
[Fire Notifications for Background Processing Events (C#)](Fire_Notification_for_Background_Processing_Events_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
