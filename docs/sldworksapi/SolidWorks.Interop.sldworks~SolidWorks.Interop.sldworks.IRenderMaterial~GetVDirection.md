# GetVDirection Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetVDirection`

Obsolete. Superseded by IRenderMaterial::GetVDirection2.
Obsolete. Superseded by [IRenderMaterial::GetVDirection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetVDirection2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetVDirection( _
   ByRef VDir As System.Double _
) 
```

```

Dim instance As IRenderMaterial
Dim VDir As System.Double
 
instance.GetVDirection(VDir)
```

```

void GetVDirection( 
   out System.double VDir
)
```

```

void GetVDirection( 
   [Out] System.double VDir
) 
```

#### Parameters

*VDir*
:   Array of doubles representing the V direction of the texture-based appearance (see Remarks)

Example

The [mapping type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~MappingType.md) (surface, projection, automatic, etc.) indirectly determines the V direction. This vector is perpendicular to the U direction.

Call [IRenderMaterial::GetUDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetUDirection.md) to get the U direction of the appearance.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)  
[IRenderMaterial::SetUDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetUDirection.md)  
[IRenderMaterial::SetVDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetVDirection.md)
