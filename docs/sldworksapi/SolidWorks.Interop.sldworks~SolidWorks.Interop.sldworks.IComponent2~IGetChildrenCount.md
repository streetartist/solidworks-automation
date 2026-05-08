# IGetChildrenCount Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetChildrenCount`

Gets the number of children components for this component.
Gets the number of children components for this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetChildrenCount() As System.Integer
```

```

Dim instance As IComponent2
Dim value As System.Integer
 
value = instance.IGetChildrenCount()
```

```

System.int IGetChildrenCount()
```

```

System.int IGetChildrenCount(); 
```

#### Return Value

Number of children

Remarks

This method returns a single-level count. The [IComponent2::GetChildren](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetChildren.md) and [IComponent2::IGetChildren](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetChildren.md) do not recurse sub-assemblies.

Example

[Show All Components (VBA)](Show_All_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)
