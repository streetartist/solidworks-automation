# SetEndConditionReference Method (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndConditionReference`

Sets the reference entity that defines the end condition in a forward or reverse direction.
Sets the reference entity that defines the end condition in a forward or reverse direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetEndConditionReference( _
   ByVal Forward As System.Boolean, _
   ByVal PDisp As System.Object _
) 
```

```

Dim instance As IExtrudeFeatureData2
Dim Forward As System.Boolean
Dim PDisp As System.Object
 
instance.SetEndConditionReference(Forward, PDisp)
```

```

void SetEndConditionReference( 
   System.bool Forward,
   System.object PDisp
)
```

```

void SetEndConditionReference( 
   System.bool Forward,
   System.Object^ PDisp
) 
```

#### Parameters

*Forward*
:   True for forward direction, false for reverse

*PDisp*
:   Pointer to the reference entity

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::GetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndConditionReference.md)  
[IExtrudeFeatureData2::GetEndCondition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndCondition.md)  
[IExtrudeFeatureData2::SetEndCondition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndCondition.md)
