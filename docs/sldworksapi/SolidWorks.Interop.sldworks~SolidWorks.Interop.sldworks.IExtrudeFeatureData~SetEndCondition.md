# SetEndCondition Method (IExtrudeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~SetEndCondition`

Obsolete. Superseded by IExtrudeFeatureData2::SetEndCondition.
Obsolete. Superseded by [IExtrudeFeatureData2::SetEndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndCondition.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetEndCondition( _
   ByVal Forward As System.Boolean, _
   ByVal EndCondition As System.Integer _
) 
```

```

Dim instance As IExtrudeFeatureData
Dim Forward As System.Boolean
Dim EndCondition As System.Integer
 
instance.SetEndCondition(Forward, EndCondition)
```

```

void SetEndCondition( 
   System.bool Forward,
   System.int EndCondition
)
```

```

void SetEndCondition( 
   System.bool Forward,
   System.int EndCondition
) 
```

#### Parameters

*Forward*

*EndCondition*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.md)  
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.md)
