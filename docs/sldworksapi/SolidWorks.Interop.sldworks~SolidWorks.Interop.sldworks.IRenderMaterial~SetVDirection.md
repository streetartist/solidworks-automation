# SetVDirection Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetVDirection`

Obsolete. Superseded by IRenderMaterial::SetVDirection2.
Obsolete. Superseded by [IRenderMaterial::SetVDirection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetVDirection2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetVDirection( _
   ByRef VDir As System.Double _
) 
```

```

Dim instance As IRenderMaterial
Dim VDir As System.Double
 
instance.SetVDirection(VDir)
```

```

void SetVDirection( 
   ref System.double VDir
)
```

```

void SetVDirection( 
   System.double% VDir
) 
```

#### Parameters

*VDir*
:   Array of doubles representing the V direction of the texture-based appearance (see Remarks)

Remarks

To specify the V direction in the Y direction, set VDir to {0,1,0}.

The [mapping type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~MappingType.md) (surface, projection, automatic, etc.) indirectly determines the V direction. This vector is perpendicular to the U direction.

Call [IRenderMaterial::SetUDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetUDirection.md) to set the U direction.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)  
[IRenderMaterial::GetUDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetUDirection.md)  
[IRenderMaterial::GetVDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetVDirection.md)
