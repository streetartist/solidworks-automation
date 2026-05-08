# GetDecalsCount Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetDecalsCount`

Gets the number of decals applied to this component.
Gets the number of decals applied to this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDecalsCount() As System.Integer
```

```

Dim instance As IComponent2
Dim value As System.Integer
 
value = instance.GetDecalsCount()
```

```

System.int GetDecalsCount()
```

```

System.int GetDecalsCount(); 
```

#### Return Value

Number of decals

Remarks

Call this method before calling [IComponent2::IGetDecals](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetDecals.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetDecals.md)
