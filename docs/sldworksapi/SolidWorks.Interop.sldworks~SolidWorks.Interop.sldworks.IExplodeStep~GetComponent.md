# GetComponent Method (IExplodeStep)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponent`

Gets the specified component in this explode step.
Gets the specified component in this explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetComponent( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IExplodeStep
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetComponent(Index)
```

```

System.object GetComponent( 
   System.int Index
)
```

```

System.Object^ GetComponent( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of a component in this explode step

#### Return Value

Specified [component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) in the explode step

Remarks

Before calling this method, call [IExplodeStep::GetNumOfComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetNumOfComponents.md) to get a valid value for Index.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)  
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.md)  
[IExplodeStep::GetComponentName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponentName.md)  
[IExplodeStep::GetNumOfComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetNumOfComponents.md)  
[IExplodeStep::IGetComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~IGetComponent.md)  
[IExplodeStep::GetComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponents.md)
