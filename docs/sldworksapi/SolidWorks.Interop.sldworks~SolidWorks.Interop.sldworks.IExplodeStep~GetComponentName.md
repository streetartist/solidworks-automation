# GetComponentName Method (IExplodeStep)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponentName`

Gets the name of the specified component in this explode step.
Gets the name of the specified component in this explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetComponentName( _
   ByVal Index As System.Integer _
) As System.String
```

```

Dim instance As IExplodeStep
Dim Index As System.Integer
Dim value As System.String
 
value = instance.GetComponentName(Index)
```

```

System.string GetComponentName( 
   System.int Index
)
```

```

System.String^ GetComponentName( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the component in this explode step

#### Return Value

Name of the component

Remarks

Before calling this method, call [IExplodeStep::GetNumOfComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetNumOfComponents.md) to get a valid value for Index.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)  
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.md)  
[IExplodeStep::GetComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponents.md)
