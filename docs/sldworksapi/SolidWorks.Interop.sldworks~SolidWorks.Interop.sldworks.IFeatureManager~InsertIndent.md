# InsertIndent Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertIndent`

Inserts an indent feature using a selected target body and tool body regions.
Inserts an indent feature using a selected target body and tool body regions.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertIndent( _
   ByVal Thickness As System.Double, _
   ByVal Clearance As System.Double, _
   ByVal Exclude As System.Boolean, _
   ByVal ClrDir As System.Boolean, _
   ByVal Cut As System.Boolean, _
   ByVal CutDir As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Thickness As System.Double
Dim Clearance As System.Double
Dim Exclude As System.Boolean
Dim ClrDir As System.Boolean
Dim Cut As System.Boolean
Dim CutDir As System.Boolean
Dim value As Feature
 
value = instance.InsertIndent(Thickness, Clearance, Exclude, ClrDir, Cut, CutDir)
```

```

Feature InsertIndent( 
   System.double Thickness,
   System.double Clearance,
   System.bool Exclude,
   System.bool ClrDir,
   System.bool Cut,
   System.bool CutDir
)
```

```

Feature^ InsertIndent( 
   System.double Thickness,
   System.double Clearance,
   System.bool Exclude,
   System.bool ClrDir,
   System.bool Cut,
   System.bool CutDir
) 
```

#### Parameters

*Thickness*
:   Thickness of the indent feature

*Clearance*
:   Distance between the tool body and target body (see **Remarks**)

*Exclude*
:   True to exclude the selections, false to include the selections

*ClrDir*
:   True to leave the direction of clearance as is, false to reverse the direction of the clearance

*Cut*
:   True to cut the target body, false to not

*CutDir*
:   True to reverse the direction of the cut if the tool body is a surface, false to not

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Prior to calling this method, you must have selected the target body and tool body regions, using these selection marks:

- Target body = 1
- Tool body region = 4

Example

[Insert Indent Feature (C#)](Insert_Indent_Feature_Example_CSharp.htm)  
[Insert Indent Feature (VB.NET)](Insert_Indent_Feature_Example_VBNET.htm)  
[Insert Indent Feature (VBA)](Insert_Indent_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IIndentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.md)
