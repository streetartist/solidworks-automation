# GetTableAnnotationCount Method (IWeldmentCutListFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~GetTableAnnotationCount`

Gets the number of weldment cut list annotations for this weldment cut list table.
Gets the number of weldment cut list annotations for this weldment cut list table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTableAnnotationCount() As System.Integer
```

```

Dim instance As IWeldmentCutListFeature
Dim value As System.Integer
 
value = instance.GetTableAnnotationCount()
```

```

System.int GetTableAnnotationCount()
```

```

System.int GetTableAnnotationCount(); 
```

#### Return Value

Number of weldment cut list annotations for this weldment cut list table

Remarks

Call this method before calling [IWeldmentCutListFeature::IGetTableAnnotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~IGetTableAnnotations.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.md)  
[IWeldmentCutListFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature_members.md)  
[IWeldmentCutListFeature::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~GetTableAnnotations.md)
