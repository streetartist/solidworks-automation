# EnumExcludedComponents2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~EnumExcludedComponents2`

Gets all of the assembly components that are excluded from this section view.
Gets all of the assembly components that are excluded from this section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EnumExcludedComponents2() As EnumComponents2
```

```

Dim instance As IDrSection
Dim value As EnumComponents2
 
value = instance.EnumExcludedComponents2()
```

```

EnumComponents2 EnumExcludedComponents2()
```

```

EnumComponents2^ EnumExcludedComponents2(); 
```

#### Return Value

Pointer to the [IEnumComponents2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2.md) object

Remarks

The ability to exclude components applies only to assembly section views. This method returns NULL for section views of parts.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)  
[IDrSection::GetExcludedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetExcludedComponents.md)
