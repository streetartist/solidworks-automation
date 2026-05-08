# CreateCallout Method (IModelView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~CreateCallout`

Creates a callout on this model view.
Creates a callout on this model view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateCallout( _
   ByVal NumberOfRows As System.Integer, _
   ByVal LpHandler As System.Object _
) As Callout
```

```

Dim instance As IModelView
Dim NumberOfRows As System.Integer
Dim LpHandler As System.Object
Dim value As Callout
 
value = instance.CreateCallout(NumberOfRows, LpHandler)
```

```

Callout CreateCallout( 
   System.int NumberOfRows,
   System.object LpHandler
)
```

```

Callout^ CreateCallout( 
   System.int NumberOfRows,
   System.Object^ LpHandler
) 
```

#### Parameters

*NumberOfRows*
:   Number of rows in the callout

*LpHandler*
:   Pointer to [ISwCalloutHandler](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwCalloutHandler.md)

#### Return Value

An [ICallout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md) object

Example

[Create a Callout in a Model View (VBA)](Create_Model_View_Callouts_Example_VB.htm)  
[Create a Callout in a Model View (VB.NET)](Create_Model_View_Callouts_Example_VBNET.htm)  
[Create a Callout in a Model View (C#)](Create_Model_View_Callouts_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)
