# GetAxisType Method (IRevolveFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetAxisType`

Gets the type of axis of revolution for this revolve feature.
Gets the type of axis of revolution for this revolve feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAxisType() As System.Integer
```

```

Dim instance As IRevolveFeatureData2
Dim value As System.Integer
 
value = instance.GetAxisType()
```

```

System.int GetAxisType()
```

```

System.int GetAxisType(); 
```

#### Return Value

Type of axis as defined in [swSelectType\_e:](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

- swSelDATUMAXES
- swSelEDGES
- swSelSKETCHSEGS

Example

[Get Axis of Revolve Feature (VBA)](Get_Axis_of_Revolve_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.md)  
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.md)  
[IRevolveFeatureData2::Axis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~Axis.md)
