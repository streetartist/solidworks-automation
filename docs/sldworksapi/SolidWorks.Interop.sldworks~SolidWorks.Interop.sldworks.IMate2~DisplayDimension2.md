# DisplayDimension2 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DisplayDimension2`

Gets the specified display dimension for this mate.
Gets the specified display dimension for this mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property DisplayDimension2( _
   ByVal Index As System.Integer _
) As DisplayDimension
```

```

Dim instance As IMate2
Dim Index As System.Integer
Dim value As DisplayDimension
 
value = instance.DisplayDimension2(Index)
```

```

DisplayDimension DisplayDimension2( 
   System.int Index
) {get;}
```

```

property DisplayDimension^ DisplayDimension2 {
   DisplayDimension^ get(System.int Index);
}
```

#### Parameters

*Index*
:   Number indicating which mate's display dimension to get (see **Remarks**)

#### Property Value

[Display dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md) for the specified mate

Remarks

This property returns the first display dimension for all types of mates and the second display dimension for gear mates only.  

A gear mate has two feature dimensions whose values form the gear ratio. All other mates return NULL/Nothing for the second display dimension.

Example

[Change Dimensions of Gear Mate (VBA)](Change_Dimensions_of_Gear_Mate_Example_VB.htm)  
[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::MaximumVariation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MaximumVariation.md)  
[IMate2::MinimumVariation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MinimumVariation.md)
