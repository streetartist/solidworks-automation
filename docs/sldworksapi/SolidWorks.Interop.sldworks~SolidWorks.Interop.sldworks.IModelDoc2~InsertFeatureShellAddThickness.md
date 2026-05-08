# InsertFeatureShellAddThickness Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFeatureShellAddThickness`

Adds thickness to a face in a multi-thickness shell feature.
Adds thickness to a face in a multi-thickness shell feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertFeatureShellAddThickness( _
   ByVal Thickness As System.Double _
) 
```

```

Dim instance As IModelDoc2
Dim Thickness As System.Double
 
instance.InsertFeatureShellAddThickness(Thickness)
```

```

void InsertFeatureShellAddThickness( 
   System.double Thickness
)
```

```

void InsertFeatureShellAddThickness( 
   System.double Thickness
) 
```

#### Parameters

*Thickness*
:   Shell thickness in meters

Remarks

This method works with [IModelDoc2::InsertFeatureShell](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFeatureShell.md) to create a multi-thickness shell as follows:

1. Select the faces to remove to create the shell feature by calling [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with Marks of 1.
2. Select faces with alternate thicknesses using Marks of 2.
3. Call this method once for each of the faces selected in step 2.
4. Call IModelDoc2::InsertFeatureShell.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
