# InsertBends Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertBends`

Obsolete. Superseded by IPartDoc::InsertBends2.
Obsolete. Superseded by [IPartDoc::InsertBends2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertBends2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertBends( _
   ByVal Radius As System.Double, _
   ByVal UseBendTable As System.String, _
   ByVal UseKfactor As System.Double, _
   ByVal UseBendAllowance As System.Double, _
   ByVal UseAutoRelief As System.Boolean, _
   ByVal OffsetRatio As System.Double _
) As System.Boolean
```

```

Dim instance As IPartDoc
Dim Radius As System.Double
Dim UseBendTable As System.String
Dim UseKfactor As System.Double
Dim UseBendAllowance As System.Double
Dim UseAutoRelief As System.Boolean
Dim OffsetRatio As System.Double
Dim value As System.Boolean
 
value = instance.InsertBends(Radius, UseBendTable, UseKfactor, UseBendAllowance, UseAutoRelief, OffsetRatio)
```

```

System.bool InsertBends( 
   System.double Radius,
   System.string UseBendTable,
   System.double UseKfactor,
   System.double UseBendAllowance,
   System.bool UseAutoRelief,
   System.double OffsetRatio
)
```

```

System.bool InsertBends( 
   System.double Radius,
   System.String^ UseBendTable,
   System.double UseKfactor,
   System.double UseBendAllowance,
   System.bool UseAutoRelief,
   System.double OffsetRatio
) 
```

#### Parameters

*Radius*

*UseBendTable*

*UseKfactor*

*UseBendAllowance*

*UseAutoRelief*

*OffsetRatio*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)
