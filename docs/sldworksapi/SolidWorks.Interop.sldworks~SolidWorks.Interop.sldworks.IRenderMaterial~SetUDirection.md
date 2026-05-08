# SetUDirection Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetUDirection`

Obsolete. Superseded by IRenderMaterial::SetUDirection2.
Obsolete. Superseded by [IRenderMaterial::SetUDirection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetUDirection2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetUDirection( _
   ByRef UDir As System.Double _
) 
```

```

Dim instance As IRenderMaterial
Dim UDir As System.Double
 
instance.SetUDirection(UDir)
```

```

void SetUDirection( 
   ref System.double UDir
)
```

```

void SetUDirection( 
   System.double% UDir
) 
```

#### Parameters

*UDir*
:   Array of doubles representing the U direction for the texture-based appearance (see **Remarks**)

Remarks

To specify the U direction in the X direction, set UDir to {1, 0, 0}.

Call [IRenderMaterial::SetVDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetVDirection.md) to set the V direction of the appearance.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)  
[IRenderMaterial::GetUDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetUDirection.md)  
[IRenderMaterial::GetVDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetVDirection.md)
