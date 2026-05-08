# IGetComponents Method (ICavityFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~IGetComponents`

Gets the design components for this cavity feature.
Gets the design components for this cavity feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetComponents( _
   ByVal Count As System.Integer, _
   ByRef Comps As Component2 _
) 
```

```

Dim instance As ICavityFeatureData
Dim Count As System.Integer
Dim Comps As Component2
 
instance.IGetComponents(Count, Comps)
```

```

void IGetComponents( 
   System.int Count,
   out Component2 Comps
)
```

```

void IGetComponents( 
   System.int Count,
   [Out] Component2^ Comps
) 
```

#### Parameters

*Count*
:   Number of design components

*Comps*
:   - in-process, unmanaged C++: Pointer to an array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) objects of size count

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ICavityFeatureData::GetComponentsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~GetComponentsCount.md) before calling this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.md)  
[ICavityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData_members.md)  
[ICavityFeatureData::ISetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~ISetComponents.md)  
[ICavityFeatureData::Components Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~Components.md)
