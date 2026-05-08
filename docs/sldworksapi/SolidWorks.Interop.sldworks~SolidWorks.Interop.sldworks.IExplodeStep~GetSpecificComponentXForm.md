# GetSpecificComponentXForm Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetSpecificComponentXForm`

Gets the transformation matrix of the specified component in this explode step.
Gets the transformation matrix of the specified component in this explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSpecificComponentXForm( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IExplodeStep
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetSpecificComponentXForm(Index)
```

```

System.object GetSpecificComponentXForm( 
   System.int Index
)
```

```

System.Object^ GetSpecificComponentXForm( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of a component in the selection list

#### Return Value

Transformation matrix array of 16 doubles

Remarks

Before calling this method, call [IExplodeStep::GetNumOfComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetNumOfComponents.md) to get a valid value for Index.

For regular explode steps, this method works just like [IExplodeStep::GetComponentXform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponentXform.md) to get the transformation of the entire explode step. This method also works for radial explode steps by getting the transformation of an individual radial explode component.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)  
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.md)
