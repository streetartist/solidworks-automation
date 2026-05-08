# BackgroundProcessingOption Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~BackgroundProcessingOption`

Gets or sets the background processing option for this drawing.
Gets or sets the background processing option for this drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BackgroundProcessingOption As System.Integer
```

```

Dim instance As IDrawingDoc
Dim value As System.Integer
 
instance.BackgroundProcessingOption = value
 
value = instance.BackgroundProcessingOption
```

```

System.int BackgroundProcessingOption {get; set;}
```

```

property System.int BackgroundProcessingOption {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Background processing option as defined in [swBackgroundProcessOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBackgroundProcessOption_e.html) (see **Remarks**)

Remarks

SOLIDWORKS recommends that you only use this property with [ISldWorks::IsBackgroundProcessingCompleted](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsBackgroundProcessingCompleted.md) and [ISldWorks::EnableBackgroundProcessing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnableBackgroundProcessing.md) when you can quickly open a drawing document via the user interface, but that same drawing takes significantly more time to open programmatically.

To more efficiently and programmatically open a drawing document that requires a lot of CPU time and no user input:

1. Set ISldWorks::EnableBackgroundProcessing to true.
2. Use [ISldWorks Event BackgroundProcessingStartNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_BackgroundProcessingStartNotifyEventHandler.md) to handle the background processing start event.
3. Open the drawing document by calling either [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md) or [ISldWorks::OpenDoc7](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.md).
4. Set IDrawingDoc::BackgroundProcessingOption to [swBackgroundProcessOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBackgroundProcessOption_e.html).swBackgroundProcessing\_DeferToApplication.
5. Call ISldWorks::IsBackgroundProcessingCompleted repeatedly, which polls the status of the open operation
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

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
