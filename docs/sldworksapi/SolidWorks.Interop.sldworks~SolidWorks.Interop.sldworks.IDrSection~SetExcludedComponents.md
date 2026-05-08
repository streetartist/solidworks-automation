# SetExcludedComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetExcludedComponents`

Excludes the specified components from this section view.
Excludes the specified components from this section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetExcludedComponents( _
   ByVal VComponents As System.Object _
) As System.Boolean
```

```

Dim instance As IDrSection
Dim VComponents As System.Object
Dim value As System.Boolean
 
value = instance.SetExcludedComponents(VComponents)
```

```

System.bool SetExcludedComponents( 
   System.object VComponents
)
```

```

System.bool SetExcludedComponents( 
   System.Object^ VComponents
) 
```

#### Parameters

*VComponents*
:   Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

#### Return Value

True if the specified components are excluded, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)  
[IDrSection::EnumExcludedComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~EnumExcludedComponents2.md)  
[IDrSection::GetExcludedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetExcludedComponents.md)  
[IDrSection::ISetExcludedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ISetExcludedComponents.md)
