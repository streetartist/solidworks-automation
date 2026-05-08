# EndCondition Property (ICoreFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~EndCondition`

Gets or sets the end condition in the specified direction for this core feature.
Gets or sets the end condition in the specified direction for this core feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EndCondition( _
   ByVal Index As System.Integer _
) As System.Integer
```

```

Dim instance As ICoreFeatureData
Dim Index As System.Integer
Dim value As System.Integer
 
instance.EndCondition(Index) = value
 
value = instance.EndCondition(Index)
```

```

System.int EndCondition( 
   System.int Index
) {get; set;}
```

```

property System.int EndCondition {
   System.int get(System.int Index);
   void set (System.int Index, System.int value);
}
```

#### Parameters

*Index*
:   Direction of end conditions as defined in [swCoreFeatureDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCoreFeatureDirection_e.html)

#### Property Value

Type of end conditions as defined in [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html) (see **Remarks**)

Remarks

Valid end conditions are swEndConditions\_e:

- swEndCondBlind
- swEndCondThroughAll
- swEndCondThroughNext

Example

[Get Core Feature Data (C#)](Get_Core_Feature_Example_CSharp.htm)  
[Get Core Feature Data (VB.NET)](Get_Core_Feature_Example_VBNET.htm)  
[Get Core Feature Data (VBA)](Get_Core_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.md)  
[ICoreFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData_members.md)
