# GetAllDecalProperties Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetAllDecalProperties`

Gets all of the decal properties applied to this face in a part.
Gets all of the decal properties applied to this face in a part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAllDecalProperties() As System.Object
```

```

Dim instance As IFace2
Dim value As System.Object
 
value = instance.GetAllDecalProperties()
```

```

System.object GetAllDecalProperties()
```

```

System.Object^ GetAllDecalProperties(); 
```

#### Return Value

Array of [decal properties applied to this face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.md)

Example

[Add Decal (C#)](Add_Decal_Example_CSharp.htm)  
[Add Decal (VB.NET)](Add_Decal_Example_VBNET.htm)  
[Add Decal (VBA)](Add_Decal_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::GetDecalsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetDecalsCount.md)  
[IFace2::GetAllAssemblyDecalProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetAllAssemblyDecalProperties.md)
