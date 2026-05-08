# MateEntityType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace~MateEntityType`

Gets the type of entity in this Inplace mate.
Gets the type of entity in this Inplace mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property MateEntityType( _
   ByVal NIndex As System.Integer _
) As System.Integer
```

```

Dim instance As IMateInPlace
Dim NIndex As System.Integer
Dim value As System.Integer
 
value = instance.MateEntityType(NIndex)
```

```

System.int MateEntityType( 
   System.int NIndex
) {get;}
```

```

property System.int MateEntityType {
   System.int get(System.int NIndex);
}
```

#### Parameters

*NIndex*
:   0-based index associated with this entity

#### Property Value

Type of entity as defined by [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

Remarks

To get the name of the entity, call [IMateInPlace::MateEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace~MateEntity.md).

Example

[Get Component Names and Types for Inplace Mate (VBA)](Get_Component_Names_and_Types_for_Inplace_Mate_Example_VB.htm)  
[Get Mates (C#)](Get_Mates_Example_CSharp.htm)  
[Get Mates (VB.NET)](Get_Mates_Example_VBNET.htm)  
[Get Mates (VBA)](Get_Mates_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateInPlace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace.md)  
[IMateInPlace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace_members.md)
