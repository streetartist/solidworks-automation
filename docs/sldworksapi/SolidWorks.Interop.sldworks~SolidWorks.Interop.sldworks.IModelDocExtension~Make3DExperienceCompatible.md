# Make3DExperienceCompatible Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Make3DExperienceCompatible`

Makes the current model compatible with SOLIDWORKS Connected.
Makes the current model compatible with [SOLIDWORKS Connected](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Make3DExperienceCompatible( _
   ByVal IncludeComponents As System.Boolean, _
   ByRef Result As System.Boolean _
) 
```

```

Dim instance As IModelDocExtension
Dim IncludeComponents As System.Boolean
Dim Result As System.Boolean
 
instance.Make3DExperienceCompatible(IncludeComponents, Result)
```

```

void Make3DExperienceCompatible( 
   System.bool IncludeComponents,
   out System.bool Result
)
```

```

void Make3DExperienceCompatible( 
   System.bool IncludeComponents,
   [Out] System.bool Result
) 
```

#### Parameters

*IncludeComponents*
:   True to make components compatible with 3DExperience, false to not

*Result*
:   True if model successfully made compatible with 3DExperience, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
