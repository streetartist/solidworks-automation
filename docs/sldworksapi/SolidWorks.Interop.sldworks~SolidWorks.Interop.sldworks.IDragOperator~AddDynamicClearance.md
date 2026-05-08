# AddDynamicClearance Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~AddDynamicClearance`

Adds a dynamic clearance detector.
Adds a dynamic clearance detector.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddDynamicClearance( _
   ByVal Comp1 As System.Object, _
   ByVal Comp2 As System.Object, _
   ByVal Value As System.Double, _
   ByVal AppendFlag As System.Boolean, _
   ByVal ShowDim As System.Boolean _
) As System.Integer
```

```

Dim instance As IDragOperator
Dim Comp1 As System.Object
Dim Comp2 As System.Object
Dim Value As System.Double
Dim AppendFlag As System.Boolean
Dim ShowDim As System.Boolean
Dim value As System.Integer
 
value = instance.AddDynamicClearance(Comp1, Comp2, Value, AppendFlag, ShowDim)
```

```

System.int AddDynamicClearance( 
   System.object Comp1,
   System.object Comp2,
   System.double Value,
   System.bool AppendFlag,
   System.bool ShowDim
)
```

```

System.int AddDynamicClearance( 
   System.Object^ Comp1,
   System.Object^ Comp2,
   System.double Value,
   System.bool AppendFlag,
   System.bool ShowDim
) 
```

#### Parameters

*Comp1*
:   First component of the clearance pair

*Comp2*
:   Second component of the clearance pair

*Value*
:   Minimum clearance distance

*AppendFlag*
:   True appends the component to the list, false overwrites the list

*ShowDim*
:   True displays a dynamic reference dimension of the minimum clearance distance

#### Return Value

Newly added clearance pair

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.md)  
[IDragOperator::IAddDynamicClearance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IAddDynamicClearance.md)  
[IDragOperator::DynamicClearanceEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DynamicClearanceEnabled.md)
