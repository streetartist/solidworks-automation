# GetVDirection2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetVDirection2`

Gets the V direction of the texture-based appearance.
Gets the V direction of the texture-based appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetVDirection2( _
   ByRef VDir_X As System.Double, _
   ByRef VDir_Y As System.Double, _
   ByRef VDir_Z As System.Double _
) 
```

```

Dim instance As IRenderMaterial
Dim VDir_X As System.Double
Dim VDir_Y As System.Double
Dim VDir_Z As System.Double
 
instance.GetVDirection2(VDir_X, VDir_Y, VDir_Z)
```

```

void GetVDirection2( 
   out System.double VDir_X,
   out System.double VDir_Y,
   out System.double VDir_Z
)
```

```

void GetVDirection2( 
   [Out] System.double VDir_X,
   [Out] System.double VDir_Y,
   [Out] System.double VDir_Z
) 
```

#### Parameters

*VDir\_X*
:   X coordinate of the V direction

*VDir\_Y*
:   Y coordinate of the V direction

*VDir\_Z*
:   Z coordinate of the V direction

Remarks

The [mapping type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~MappingType.md) (surface, projection, automatic, etc.) indirectly determines the V direction. This vector is perpendicular to the U direction.

Call [IRenderMaterial::GetUDirection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetUDirection2.md) to get the U direction of the appearance.

Example

See [IRenderMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)  
[IRenderMaterial::SetUDirection2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetUDirection2.md)  
[IRenderMaterial::SetVDirection2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetVDirection2.md)
