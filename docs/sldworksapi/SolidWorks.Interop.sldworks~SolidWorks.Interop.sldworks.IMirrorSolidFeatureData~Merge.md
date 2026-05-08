# Merge Property (IMirrorSolidFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~Merge`

Gets or sets the merge results option for the mirrored solid feature in a multibody part.
Gets or sets the merge results option for the mirrored solid feature in a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Merge As System.Boolean
```

```

Dim instance As IMirrorSolidFeatureData
Dim value As System.Boolean
 
instance.Merge = value
 
value = instance.Merge
```

```

System.bool Merge {get; set;}
```

```

property System.bool Merge {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True enables the merge results option, false does not

Remarks

The merge results option tells the SOLIDWORKS software whether to merge the new body or bodies with existing bodies in the multibody part. This property is set to True by default.

Example

[Get Mirror Solid Feature Data (C#)](Get_Mirror_Solid_Feature_Data_Example_CSharp.htm)  
[Get Mirror Solid Feature Data (VB.NET)](Get_Mirror_Solid_Feature_Data_Example_VBNET.htm)  
[Get Mirror Solid Feature Data (VBA)](Get_Mirror_Solid_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData.md)  
[IMirrorSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData_members.md)
