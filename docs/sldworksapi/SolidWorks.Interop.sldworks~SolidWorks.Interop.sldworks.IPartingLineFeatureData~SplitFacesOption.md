# SplitFacesOption Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SplitFacesOption`

Gets or sets the split faces option for this parting line.
Gets or sets the split faces option for this parting line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SplitFacesOption As System.Integer
```

```

Dim instance As IPartingLineFeatureData
Dim value As System.Integer
 
instance.SplitFacesOption = value
 
value = instance.SplitFacesOption
```

```

System.int SplitFacesOption {get; set;}
```

```

property System.int SplitFacesOption {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Split faces option as defined in [swSplitFacesOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSplitFacesOption_e.html)

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
[SplitFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SplitFaces.md)  
[GetEntitiesToSplit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetEntitiesToSplit.md)  
[GetEntitiesToSplitCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetEntitiesToSplitCount.md)  
[IGetEntitiesToSplit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~IGetEntitiesToSplit.md)  
[ISetEntitiesToSplit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~ISetEntitiesToSplit.md)  
[IPartingLineFeatureData::SetEntitiesToSplit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SetEntitiesToSplit.md)
