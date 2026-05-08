# InsertBends2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertBends2`

Creates bends in a thin-feature part.
Creates bends in a thin-feature part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertBends2( _
   ByVal Radius As System.Double, _
   ByVal UseBendTable As System.String, _
   ByVal UseKfactor As System.Double, _
   ByVal UseBendAllowance As System.Double, _
   ByVal UseAutoRelief As System.Boolean, _
   ByVal OffsetRatio As System.Double, _
   ByVal DoFlatten As System.Boolean _
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
Dim DoFlatten As System.Boolean
Dim value As System.Boolean
 
value = instance.InsertBends2(Radius, UseBendTable, UseKfactor, UseBendAllowance, UseAutoRelief, OffsetRatio, DoFlatten)
```

```

System.bool InsertBends2( 
   System.double Radius,
   System.string UseBendTable,
   System.double UseKfactor,
   System.double UseBendAllowance,
   System.bool UseAutoRelief,
   System.double OffsetRatio,
   System.bool DoFlatten
)
```

```

System.bool InsertBends2( 
   System.double Radius,
   System.String^ UseBendTable,
   System.double UseKfactor,
   System.double UseBendAllowance,
   System.bool UseAutoRelief,
   System.double OffsetRatio,
   System.bool DoFlatten
) 
```

#### Parameters

*Radius*
:   Radius of the bends

*UseBendTable*
:   Bend table name (.btl file)

*UseKfactor*
:   K-Factor ratio or -1 if not used

*UseBendAllowance*
:   Bend allowance value or -1 if not used

*UseAutoRelief*
:   True if auto-relief cuts are to be added, false if not

*OffsetRatio*
:   Distance relief cut extends beyond bend (see **Remarks)**

*DoFlatten*
:   True to create these three features: Sheet-Metal, Flatten-Bends, and Process-Bends, false to create only the Sheet-Metal feature

#### Return Value

True if successful, false if not

Remarks

The offsetRatio argument is from 0.05 to 2.0.  Any other value fails to create the  
bend features.

When True is passed to doFlatten, all three Sheet-Metal features are created.

For more information on these arguments, see SOLIDWORKS Help.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)
