# SetVDirection2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetVDirection2`

Sets the V direction of the texture-based appearance.
Sets the V direction of the texture-based appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetVDirection2( _
   ByVal VDir_X As System.Double, _
   ByVal VDir_Y As System.Double, _
   ByVal VDir_Z As System.Double _
) 
```

```

Dim instance As IRenderMaterial
Dim VDir_X As System.Double
Dim VDir_Y As System.Double
Dim VDir_Z As System.Double
 
instance.SetVDirection2(VDir_X, VDir_Y, VDir_Z)
```

```

void SetVDirection2( 
   System.double VDir_X,
   System.double VDir_Y,
   System.double VDir_Z
)
```

```

void SetVDirection2( 
   System.double VDir_X,
   System.double VDir_Y,
   System.double VDir_Z
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

To specify the V direction in the Y direction, set:

1. VDir\_X to 0.0.
2. VDir\_Y to 1.0.
3. VDir\_Z to 0.0.

The [mapping type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~MappingType.md) (surface, projection, automatic, etc.) indirectly determines the V direction. This vector is perpendicular to the U direction.

Call [IRenderMaterial::SetUDirection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetUDirection2.md) to set the U direction.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)  
[IRenderMaterial::GetUDirection2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetUDirection2.md)  
[IRenderMaterial::GetVDirection2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetVDirection2.md)
