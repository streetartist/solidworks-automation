# IsVirtualComponent2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsVirtualComponent2`

Obsolete. Superseded by IModelDocExtension::IsVirtualComponent3.
Obsolete. Superseded by [IModelDocExtension::IsVirtualComponent3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsVirtualComponent3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsVirtualComponent2() As System.Object
```

```

Dim instance As IModelDocExtension
Dim value As System.Object
 
value = instance.IsVirtualComponent2()
```

```

System.object IsVirtualComponent2()
```

```

System.Object^ IsVirtualComponent2(); 
```

#### Return Value

Fully qualified paths to parent assembly components, up to and including the first non-virtual parent assembly component, if the model is a virtual component

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IComponent2::IsVirtual Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsVirtual.md)
