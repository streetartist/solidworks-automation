# SetUDirection2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetUDirection2`

Sets the U direction of the texture-based appearance.
Sets the U direction of the texture-based appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetUDirection2( _
   ByVal UDir_X As System.Double, _
   ByVal UDir_Y As System.Double, _
   ByVal UDir_Z As System.Double _
) 
```

```

Dim instance As IRenderMaterial
Dim UDir_X As System.Double
Dim UDir_Y As System.Double
Dim UDir_Z As System.Double
 
instance.SetUDirection2(UDir_X, UDir_Y, UDir_Z)
```

```

void SetUDirection2( 
   System.double UDir_X,
   System.double UDir_Y,
   System.double UDir_Z
)
```

```

void SetUDirection2( 
   System.double UDir_X,
   System.double UDir_Y,
   System.double UDir_Z
) 
```

#### Parameters

*UDir\_X*
:   X coordinate of the U direction

*UDir\_Y*
:   Y coordinate of the U direction

*UDir\_Z*
:   Z coordinate of the U direction

Remarks

To specify the U direction in the X direction, set:

1. UDir\_X to 1.0.
2. UDir\_Y to 0.0.
3. UDir\_Z to 0.0.

Call [IRenderMaterial::SetVDirection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetVDirection2.md) to set the V direction of the appearance.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)  
[IRenderMaterial::GetUDirection2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetUDirection2.md)  
[IRenderMaterial::GetVDirection2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetVDirection2.md)
