# GetUDirection2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetUDirection2`

Gets the U direction of the texture-based appearance.
Gets the U direction of the texture-based appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetUDirection2( _
   ByRef UDir_X As System.Double, _
   ByRef UDir_Y As System.Double, _
   ByRef UDir_Z As System.Double _
) 
```

```

Dim instance As IRenderMaterial
Dim UDir_X As System.Double
Dim UDir_Y As System.Double
Dim UDir_Z As System.Double
 
instance.GetUDirection2(UDir_X, UDir_Y, UDir_Z)
```

```

void GetUDirection2( 
   out System.double UDir_X,
   out System.double UDir_Y,
   out System.double UDir_Z
)
```

```

void GetUDirection2( 
   [Out] System.double UDir_X,
   [Out] System.double UDir_Y,
   [Out] System.double UDir_Z
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

Call [IRenderMaterial::GetVDirection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetVDirection2.md) to get the V direction of the appearance.

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
