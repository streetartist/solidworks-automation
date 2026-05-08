# GetRenderMaterialsCount Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRenderMaterialsCount`

Obsolete. Superseded by IComponent2::GetRenderMaterialsCount2.
Obsolete. Superseded by [IComponent2::GetRenderMaterialsCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRenderMaterialsCount2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRenderMaterialsCount() As System.Integer
```

```

Dim instance As IComponent2
Dim value As System.Integer
 
value = instance.GetRenderMaterialsCount()
```

```

System.int GetRenderMaterialsCount()
```

```

System.int GetRenderMaterialsCount(); 
```

#### Return Value

Number of appearances

Remarks

Call this method before calling [IComponent::IGetRenderMaterials](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetRenderMaterials.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetRenderMaterials Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRenderMaterials.md)
