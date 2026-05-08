# ISetExcludedComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ISetExcludedComponents`

Excludes the specified components from this section view.
Excludes the specified components from this section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetExcludedComponents( _
   ByVal Number As System.Integer, _
   ByRef LpComps As Component _
) As System.Boolean
```

```

Dim instance As IDrSection
Dim Number As System.Integer
Dim LpComps As Component
Dim value As System.Boolean
 
value = instance.ISetExcludedComponents(Number, LpComps)
```

```

System.bool ISetExcludedComponents( 
   System.int Number,
   ref Component LpComps
)
```

```

System.bool ISetExcludedComponents( 
   System.int Number,
   Component^% LpComps
) 
```

#### Parameters

*Number*
:   Number of components

*LpComps*
:   - in-process, unmanaged C++: Pointer to array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) objects of size Number

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

True if the specified components are excluded, false if not

Remarks

Call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) after calling this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)  
[IDrSection::EnumExcludedComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~EnumExcludedComponents2.md)  
[IDrSection::GetExcludedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetExcludedComponents.md)  
[IDrSection::SetExcludedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetExcludedComponents.md)
