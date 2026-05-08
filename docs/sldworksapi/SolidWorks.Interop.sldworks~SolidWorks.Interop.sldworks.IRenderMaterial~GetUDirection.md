# GetUDirection Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetUDirection`

Obsolete. Superseded by IRenderMaterial::GetUDirection2.
Obsolete. Superseded by [IRenderMaterial::GetUDirection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetUDirection2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetUDirection( _
   ByRef UDir As System.Double _
) 
```

```

Dim instance As IRenderMaterial
Dim UDir As System.Double
 
instance.GetUDirection(UDir)
```

```

void GetUDirection( 
   out System.double UDir
)
```

```

void GetUDirection( 
   [Out] System.double UDir
) 
```

#### Parameters

*UDir*
:   Array of doubles representing the U direction for the texture-based appearance (see Remarks)

Remarks

Call [IRenderMaterial::GetVDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetVDirection.md) to get the V direction of the appearance.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)  
[IRenderMaterial::SetUDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetUDirection.md)  
[IRenderMaterial::SetVDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetVDirection.md)
