# HasLegacyCThreads Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasLegacyCThreads`

Gets whether this model has legacy cosmetic threads.
Gets whether this model has legacy cosmetic threads.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function HasLegacyCThreads() As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim value As System.Boolean
 
value = instance.HasLegacyCThreads()
```

```

System.bool HasLegacyCThreads()
```

```

System.bool HasLegacyCThreads(); 
```

#### Return Value

True if the model has legacy cosmetic threads, false if not

Remarks

If this method returns true, you can call [IModelDocExtension::UpgradeLegacyCThreads](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpgradeLegacyCThreads.md) to upgrade cosmetic thread features to the latest cosmetic thread architecture.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[ICThread Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread.md)  
[IView::GetCThreads Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCThreads.md)  
[IView::GetFirstCThread Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCThread.md)
