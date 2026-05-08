# MinimumVariation Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MinimumVariation`

Gets the minimum variation, in meters or radians, for the dimension of this distance or angle mate.
Gets the minimum variation, in meters or radians, for the dimension of this distance or angle mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property MinimumVariation As System.Double
```

```

Dim instance As IMate2
Dim value As System.Double
 
value = instance.MinimumVariation
```

```

System.double MinimumVariation {get;}
```

```

property System.double MinimumVariation {
   System.double get();
}
```

#### Property Value

Minimum variation for the dimension of this mate

Remarks

This property is valid only for [IMate2::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~Type.md):

- swMateType\_e.swMateANGLE

   - or -

- swMateType\_e.swMateDISTANCE

For distance and angle mates:

*Minimum\_variation* =  *minimum\_value - dimension\_value*

Example

[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)  
[Get Mate Definition (VBA)](Get_Mate_Definition_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::DisplayDimension2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DisplayDimension2.md)  
[IMate2::MaximumVariation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MaximumVariation.md)
