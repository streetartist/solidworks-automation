# InsertDome Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertDome`

Inserts a dome.
Inserts a dome.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertDome( _
   ByVal Height As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal DoEllipticSurface As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim Height As System.Double
Dim ReverseDir As System.Boolean
Dim DoEllipticSurface As System.Boolean
 
instance.InsertDome(Height, ReverseDir, DoEllipticSurface)
```

```

void InsertDome( 
   System.double Height,
   System.bool ReverseDir,
   System.bool DoEllipticSurface
)
```

```

void InsertDome( 
   System.double Height,
   System.bool ReverseDir,
   System.bool DoEllipticSurface
) 
```

#### Parameters

*Height*
:   Height for the dome in meters

*ReverseDir*
:   True if you want to reverse the dome direction, false if not

*DoEllipticSurface*
:   RUE if you want the dome to be an elliptical surface, false if not

Remarks

Before using this method, you must select the face for the dome using a selection mark of 1. See [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md).

Example

[Create and Modify Dome Feature (C#)](Create_and_Modify_Dome_Feature_Example_CSharp.htm)  
[Create and Modify Dome Feature (VB.NET)](Create_and_Modify_Dome_Feature_Example_VBNET.htm)  
[Create and Modify Dome Feature (VBA)](Create_and_Modify_Dome_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IDomeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.md)
