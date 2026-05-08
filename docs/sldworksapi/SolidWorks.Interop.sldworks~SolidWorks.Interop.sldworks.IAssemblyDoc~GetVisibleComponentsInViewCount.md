# GetVisibleComponentsInViewCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetVisibleComponentsInViewCount`

Gets the number of visible components in this assembly.
Gets the number of visible components in this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetVisibleComponentsInViewCount() As System.Integer
```

```

Dim instance As IAssemblyDoc
Dim value As System.Integer
 
value = instance.GetVisibleComponentsInViewCount()
```

```

System.int GetVisibleComponentsInViewCount()
```

```

System.int GetVisibleComponentsInViewCount(); 
```

#### Return Value

Number of visible components in this assembly

Remarks

Call this method before calling [IAssembly\_Doc::IGetVisibleComponentsInView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetVisibleComponentsInView.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
