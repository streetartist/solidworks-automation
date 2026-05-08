# CreateCallout2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~CreateCallout2`

Creates a callout for the selection.
Creates a callout for the selection.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateCallout2( _
   ByVal NumberOfRows As System.Integer, _
   ByVal LpHandler As System.Object _
) As Callout
```

```

Dim instance As ISelectionMgr
Dim NumberOfRows As System.Integer
Dim LpHandler As System.Object
Dim value As Callout
 
value = instance.CreateCallout2(NumberOfRows, LpHandler)
```

```

Callout CreateCallout2( 
   System.int NumberOfRows,
   System.object LpHandler
)
```

```

Callout^ CreateCallout2( 
   System.int NumberOfRows,
   System.Object^ LpHandler
) 
```

#### Parameters

*NumberOfRows*
:   Number of rows in the callout

*LpHandler*
:   Pointer to the event handler for the callout ([ISwCalloutHandler](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwCalloutHandler.md))

#### Return Value

[Callout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md)

Remarks

To create a callout independent of a selection, use [IModelDocExtension::CreateCallout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateCallout.md).

Example

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)  
[ISelectionMgr::SetCallout Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetCallout.md)
