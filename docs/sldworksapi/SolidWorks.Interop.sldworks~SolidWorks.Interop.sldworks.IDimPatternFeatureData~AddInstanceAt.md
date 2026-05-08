# AddInstanceAt Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~AddInstanceAt`

Adds a pattern instance to this variable pattern feature.
Adds a pattern instance to this variable pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddInstanceAt( _
   ByVal IsSuppressed As System.Boolean, _
   ByVal Index As System.Integer _
) As System.Boolean
```

```

Dim instance As IDimPatternFeatureData
Dim IsSuppressed As System.Boolean
Dim Index As System.Integer
Dim value As System.Boolean
 
value = instance.AddInstanceAt(IsSuppressed, Index)
```

```

System.bool AddInstanceAt( 
   System.bool IsSuppressed,
   System.int Index
)
```

```

System.bool AddInstanceAt( 
   System.bool IsSuppressed,
   System.int Index
) 
```

#### Parameters

*IsSuppressed*
:   True to suppress this pattern instance, false to not

*Index*
:   0-based index indicating where to add this pattern instance in the pattern table and pattern; -1 indicates to add this pattern instance to the end of the pattern table and pattern (see **Remarks**)

#### Return Value

True if the pattern instance is added, false if not

Remarks

Use [IDimPatternFeatureData::GetInstanceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceCount.md) to get the number of pattern instances.

By default, this pattern instance inherits the default values of the parent sketch or feature of the variable pattern feature. Use [IDimPatternFeatureData::SetInstanceDimensionValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceDimensionValue.md) to modify this pattern instance's values.

Example

[Delete and Insert Instances in Variable Pattern Feature (C#)](Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_CSharp.htm)  
[Delete and Insert Instances in Variable Pattern Feature (VB.NET)](Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_VBNET.htm)  
[Delete and Insert Instances in Variable Pattern Feature (VBA)](Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.md)  
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.md)  
[IDimPatternFeatureData::DeleteInstanceAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~DeleteInstanceAt.md)
