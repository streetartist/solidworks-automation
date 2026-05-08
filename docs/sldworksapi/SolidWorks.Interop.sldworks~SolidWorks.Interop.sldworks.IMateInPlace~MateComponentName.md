# MateComponentName Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace~MateComponentName`

Gets the name of the specified component for this Inplace mate.
Gets the name of the specified component for this **Inplace** mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property MateComponentName( _
   ByVal NIndex As System.Integer _
) As System.String
```

```

Dim instance As IMateInPlace
Dim NIndex As System.Integer
Dim value As System.String
 
value = instance.MateComponentName(NIndex)
```

```

System.string MateComponentName( 
   System.int NIndex
) {get;}
```

```

property System.String^ MateComponentName {
   System.String^ get(System.int NIndex);
}
```

#### Parameters

*NIndex*
:   0-based index associated with the specified component

#### Property Value

Name of the specified component

Example

[Get Component Names and Types for Inplace MAte (VBA)](Get_Component_Names_and_Types_for_Inplace_Mate_Example_VB.htm)  
[Get Mates (C#)](Get_Mates_Example_CSharp.htm)  
[Get Mates (VB.NET)](Get_Mates_Example_VBNET.htm)  
[Get Mates (VBA)](Get_Mates_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateInPlace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace.md)  
[IMateInPlace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace_members.md)
