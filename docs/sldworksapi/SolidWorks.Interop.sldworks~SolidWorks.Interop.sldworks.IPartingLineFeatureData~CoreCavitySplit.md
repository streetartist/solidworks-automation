# CoreCavitySplit Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~CoreCavitySplit`

Gets or sets the core/cavity split option for a parting line.
Gets or sets the core/cavity split option for a parting line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CoreCavitySplit As System.Boolean
```

```

Dim instance As IPartingLineFeatureData
Dim value As System.Boolean
 
instance.CoreCavitySplit = value
 
value = instance.CoreCavitySplit
```

```

System.bool CoreCavitySplit {get; set;}
```

```

property System.bool CoreCavitySplit {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enable a core/cavity split, false to not

Example

[Set Options for Parting Line (VBA)](Set_Split_Faces_Option_for_Parting_Line_Example_VB.htm)  
[Get and Set Parting Line Feature Data (C#)](Get_and_Set_Parting_Line_Feature_Data_Example_CSharp.htm)  
[Get and Set Parting Line Feature Data (VB.NET)](Get_and_Set_Parting_Line_Feature_Data_Example_VBNET.htm)  
[Get and Set Parting Line Feature Data (VBA)](Get_and_Set_Parting_Line_Feature_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.md)  
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.md)
