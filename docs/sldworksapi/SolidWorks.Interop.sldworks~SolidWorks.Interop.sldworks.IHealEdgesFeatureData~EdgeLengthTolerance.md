# EdgeLengthTolerance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~EdgeLengthTolerance`

Gets or sets the maximum length of the edges to merge.
Gets or sets the maximum length of the edges to merge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EdgeLengthTolerance As System.Double
```

```

Dim instance As IHealEdgesFeatureData
Dim value As System.Double
 
instance.EdgeLengthTolerance = value
 
value = instance.EdgeLengthTolerance
```

```

System.double EdgeLengthTolerance {get; set;}
```

```

property System.double EdgeLengthTolerance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Maximum length of the edges to merge

Example

[Get Heal Edges Feature Data (C#)](Get_Heal_Edges_Feature_Data_Example_CSharp.htm)  
[Get Heal Edges Feature Data (VB.NET)](Get_Heal_Edges_Feature_Data_Example_VBNET.htm)  
[Get Heal Edges Feature Data (VBA)](Get_Heal_Edges_Feature_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHealEdgesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData.md)  
[IHealEdgesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData_members.md)
