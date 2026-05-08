# GetEndConditionReference Method (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndConditionReference`

Gets the reference entity defining the end condition in the forward or reverse direction.
Gets the reference entity defining the end condition in the forward or reverse direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEndConditionReference( _
   ByVal Forward As System.Boolean, _
   ByRef ReferenceType As System.Integer _
) As System.Object
```

```

Dim instance As IExtrudeFeatureData2
Dim Forward As System.Boolean
Dim ReferenceType As System.Integer
Dim value As System.Object
 
value = instance.GetEndConditionReference(Forward, ReferenceType)
```

```

System.object GetEndConditionReference( 
   System.bool Forward,
   out System.int ReferenceType
)
```

```

System.Object^ GetEndConditionReference( 
   System.bool Forward,
   [Out] System.int ReferenceType
) 
```

#### Parameters

*Forward*
:   True for forward direction, false for reverse

*ReferenceType*
:   Reference type as defined by [swSelectionReferenceTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectionReferenceTypes_e.html)

#### Return Value

Pointer to the reference entity

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::SetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndConditionReference.md)  
[IExtrudeFeatureData2::SetEndCondition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndCondition.md)  
[IExtrudeFeatureData2::GetEndCondition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndCondition.md)
