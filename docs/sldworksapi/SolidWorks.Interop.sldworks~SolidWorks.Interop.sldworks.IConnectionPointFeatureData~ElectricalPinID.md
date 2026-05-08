# ElectricalPinID Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData~ElectricalPinID`

Gets and sets the electrical pin ID of this connection point feature.
Gets and sets the electrical pin ID of this connection point feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ElectricalPinID As System.String
```

```

Dim instance As IConnectionPointFeatureData
Dim value As System.String
 
instance.ElectricalPinID = value
 
value = instance.ElectricalPinID
```

```

System.string ElectricalPinID {get; set;}
```

```

property System.String^ ElectricalPinID {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Electrical pin ID

Example

[Get and Set Connection Point Feature Data (VBA)](Get_and_Set_Connection_Point_Feature_Data_Example_VB.htm)  
[Get and Set Connection Point Feature Data (VB.NET)](Get_and_Set_Connection_Point_Feature_Data_Example_VBNET.htm)  
[Get and Set Connection Point Feature Data (C#)](Get_and_Set_Connection_Point_Feature_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConnectionPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData.md)  
[IConnectionPointFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData_members.md)
