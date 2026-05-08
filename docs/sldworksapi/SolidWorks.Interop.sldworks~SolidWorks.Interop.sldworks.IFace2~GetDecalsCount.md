# GetDecalsCount Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetDecalsCount`

Gets the number of decals applied to this face.
Gets the number of decals applied to this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDecalsCount() As System.Integer
```

```

Dim instance As IFace2
Dim value As System.Integer
 
value = instance.GetDecalsCount()
```

```

System.int GetDecalsCount()
```

```

System.int GetDecalsCount(); 
```

#### Return Value

Number of decals applied to this face

Remarks

Call this method before calling [IFace2::IGetAllDecalProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetAllDecalProperties.md) to get the size of the array for that method.

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
[IFae2::GetAllDecalProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetAllDecalProperties.md)  
[IFace2::IGetDecalProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetDecalProperties.md)  
[IFace2::IGetDecalProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetDecalProperties.md)
