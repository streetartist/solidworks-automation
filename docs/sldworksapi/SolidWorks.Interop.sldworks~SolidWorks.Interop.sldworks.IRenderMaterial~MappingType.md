# MappingType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~MappingType`

Gets or sets the mapping type for this appearance.
Gets or sets the mapping type for this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MappingType As System.Integer
```

```

Dim instance As IRenderMaterial
Dim value As System.Integer
 
instance.MappingType = value
 
value = instance.MappingType
```

```

System.int MappingType {get; set;}
```

```

property System.int MappingType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

- 0 = Surface

1 = Projection

2  = Spherical

3 = Cylindrical

4 = Automatic

Example

See the "Add Decal" examples in [IRenderMaterial::FileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~FileName.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
