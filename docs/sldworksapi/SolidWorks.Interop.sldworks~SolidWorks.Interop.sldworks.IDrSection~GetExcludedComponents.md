# GetExcludedComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetExcludedComponents`

Gets all of the assembly components that are excluded from this section view.
Gets all of the assembly components that are excluded from this section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetExcludedComponents() As System.Object
```

```

Dim instance As IDrSection
Dim value As System.Object
 
value = instance.GetExcludedComponents()
```

```

System.object GetExcludedComponents()
```

```

System.Object^ GetExcludedComponents(); 
```

#### Return Value

Array of excluded [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)  
[IDrSection::EnumExcludedComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~EnumExcludedComponents2.md)  
[IDrSection::ISetExcludedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ISetExcludedComponents.md)  
[IDrSection::SetExcludedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetExcludedComponents.md)
