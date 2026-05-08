# GetTableAnnotationCount Method (IRevisionTableFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature~GetTableAnnotationCount`

Gets the number of revision table annotations for this revision table.
Gets the number of revision table annotations for this revision table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTableAnnotationCount() As System.Integer
```

```

Dim instance As IRevisionTableFeature
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

Number of revision table annotations

Remarks

Call this method before calling [IRevisionTableFeature::IGetTableAnnotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature~IGetTableAnnotations.md) to get the size of the array for that method.

Example

See the [IRevisionTableFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevisionTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature.md)  
[IRevisionTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature_members.md)  
[IRevisionTableFeature::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature~GetTableAnnotations.md)
