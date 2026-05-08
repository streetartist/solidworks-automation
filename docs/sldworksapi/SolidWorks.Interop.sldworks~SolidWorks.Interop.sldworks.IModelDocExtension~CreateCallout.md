# CreateCallout Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateCallout`

Creates a callout independent of a selection.
Creates a callout independent of a selection.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateCallout( _
   ByVal NumberOfRows As System.Integer, _
   ByVal Handler As System.Object _
) As Callout
```

```

Dim instance As IModelDocExtension
Dim NumberOfRows As System.Integer
Dim Handler As System.Object
Dim value As Callout
 
value = instance.CreateCallout(NumberOfRows, Handler)
```

```

Callout CreateCallout( 
   System.int NumberOfRows,
   System.object Handler
)
```

```

Callout^ CreateCallout( 
   System.int NumberOfRows,
   System.Object^ Handler
) 
```

#### Parameters

*NumberOfRows*
:   Number of rows in the callout

*Handler*
:   Pointer to the event handler for the callout ([ISwCalloutHandler](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwCalloutHandler.md))

#### Return Value

[Callout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md)

Remarks

This method allows you to create a callout independently of a selection. You can define the position of the callout using the [ICallout::Position](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~Position.md) and [ICallout::SetTargetPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~SetTargetPoint.md).

To create a callout dependent on a selection, use [ISelectionMgr::CreateCallout2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~CreateCallout2.md).

Example

[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)  
[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)  
[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
